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
    manager=ManagerSerializer()


    class Meta:
        model = Employee
        fields = ['first_name','last_name','hire_date','manager', 'job_id','manager']

    def create(self, validated_data):
        jobid = validated_data.pop('job_id')
        manag=validated_data.pop('manager')

        job=JobSerializer.create(JobSerializer(),validated_data=jobid)
        manager = ManagerSerializer.create(ManagerSerializer(), validated_data=manag)
        emp= Employee.objects.create(**validated_data,manager=manager,job_id=job)

        return emp
