from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Review
from .serializers import ReviewSerializer, ReviewCreateSerializer


class ReviewView(ModelViewSet):
    queryset = Review.objects.all().order_by('-pk')
    serializer_class = ReviewSerializer
    action_serializers = {
        'create': ReviewCreateSerializer,
        'list': ReviewSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {'averages': Review.get_average(), 'frequency': Review.get_frequency(), 'count_review': queryset.count(),
             'list': serializer.data})

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if Review.is_user_exists(request.user):
            return Response(status=status.HTTP_409_CONFLICT)

        review = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED, headers=headers)
