from rest_framework import serializers

from user.models import Location, User, Employee, Job, Manager


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['first_name', 'last_name', 'phone_num', 'email', 'location_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    job_id = JobSerializer()

    class Meta:
        model = Employee
        fields = ['hire_date', 'manager', 'job_id']

    def create(self, validated_data):
        jobid = validated_data.pop('job_id')
        Job.objects.create(**jobid)

        # Employee_instance = Employee.objects.create(**validated_data)
        return Job
