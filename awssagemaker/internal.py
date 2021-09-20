import boto3


class SageMakerGroundTruthInternal:
    
    def __init__(self):
        pass
    
    def get_builder():
        """
        Description:
            | - Return Instance of SageMakerGroundTruthInternal
        Return:
            | - (type: SageMakerGroundTruthInternal())
        """
        return SageMakerGroundTruthInternal()

    def with_job_name(self, job_name):
        """
        Description:
            | - Builder method to add job name
        Params:
            | - job_name (type: str) (required) (unique for account labeling job name)
        Return:
            | - (type: SageMakerGroundTruthInternal())
        """
        self.job_name = job_name
        return self
    
    def with_labeling_team(self, labeling_team_arn):
        """
        Description:
            | - Builder method to add labeling team arn
        Params:
            | - labeling_team_arn (type: str) (required) (arn:aws:sagemaker:us-east-1:123456789012:workteam/private-crowd/labeling-team)
        Return:
            | - (type: SageMakerGroundTruthInternal())
        """
        self.labeling_team_arn = labeling_team_arn
        return self
    
    def with_preprocessing_lambda(self, preprocessing_labeling_lambda_arn):
        """
        Description:
            | - Builder method to add preprocessing labeling lambda arn
        Params:
            | - preprocessing_labeling_lambda_arn (type: str) (required) (arn:aws:lambda:us-east-1:123456789012:function:LambdaName)
        Return:
            | - (type: SageMakerGroundTruthInternal())
        """
        self.preprocessing_labeling_lambda_arn = preprocessing_labeling_lambda_arn
        return self
        
    def with_postprocessing_lambda(self, postprocessing_labeling_lambda_arn):        
        """
        Description:
            | - Builder method to add postprocessing labeling lambda arn
        Params:
            | - postprocessing_labeling_lambda_arn (type: str) (required) (arn:aws:lambda:us-east-1:123456789012:function:LambdaName)
        Return:
            | - (type: SageMakerGroundTruthInternal())
        """
        self.postprocessing_labeling_lambda_arn = postprocessing_labeling_lambda_arn
        return self
    
    def with_attribute_name(self, attribute_name):
        """
        Description:
            | - Builder method to add attribute name
        Params:
            | - attribute_name (type: str) (required) (attribute name - provide any string)
        Return:
            | - (type: SageMakerGroundTruthInternal())
        """
        self.attribute_name = attribute_name
        return self    
    
    def with_input_manifest_path(self, input_manifest_path):
        """
        Description:
            | - Builder method to add input manifest path
        Params:
            | - input_manifest_path (type: str) (required)
        Return:
            | - (type: SageMakerGroundTruthInternal())
        """
        self.input_manifest_path = input_manifest_path
        return self
    
    def with_output_manifest_path(self, output_manifest_path):
        """
        Description:
            | - Builder method to add output manifest path
        Params:
            | - output_manifest_path (type: str) (required)
        Return:
            | - (type: SageMakerGroundTruthInternal())
        """
        self.output_manifest_path = output_manifest_path
        return self
    
    def with_labeling_template_path(self, labeling_template_path):
        """
        Description:
            | - Builder method to add labeling template path
        Params:
            | - labeling_template_path (type: str) (required)
        Return:
            | - (type: SageMakerGroundTruthInternal())
        """
        self.labeling_template_path = labeling_template_path
        return self
    
    def with_task_time_limit(self, task_time_limit):
        """
        Description:
            | - Builder method to add task time limit in seconds
        Params:
            | - task_time_limit (type: str) (required) (in seconds)
        Return:
            | - (type: SageMakerGroundTruthInternal())
        """
        self.task_time_limit = task_time_limit
        return self
    
    def with_job_availability_time(self, job_availability_time):
        """
        Description:
            | - Builder method to add job availability time in seconds
        Params:
            | - job_availability_time (type: str) (required) (in seconds)
        Return:
            | - (type: SageMakerGroundTruthInternal())
        """
        self.job_availability_time = job_availability_time
        return self
    
    def with_tags(self, tags_list):
        """
        Description:
            | - Builder method to add job tags
        Params:
            | - tags_list (type: list() of dict()) (required) (f. egz [{'Key1':'value1'},{'Key2':'value2'}])
        Return:
            | - (type: SageMakerGroundTruthInternal())
        """
        self.tags = tags_list
        return self
    
    def build(self):
        """
        Description:
            | - Method to build final instance. If some property is missing, Exception raises
        Return:
            | - (type: SageMakerGroundTruthInternal())
        """
        self.__property_validation('job_name')
        self.__property_validation('labeling_team_arn')
        self.__property_validation('preprocessing_labeling_lambda_arn')
        self.__property_validation('postprocessing_labeling_lambda_arn')
        self.__property_validation('attribute_name')
        self.__property_validation('input_manifest_path')
        self.__property_validation('output_manifest_path')
        self.__property_validation('labeling_template_path')
        self.__property_validation('task_time_limit')
        self.__property_validation('job_availability_time')
        if not hasattr(self, 'tags'):
            raise Exception("Value for 'tags' not found")
        if not isinstance(self.tags, list):
            raise Exception("Value for 'tags' not found")
        if len(self.tags)==0:
            raise Exception("Value for 'tags' not found")
        if len([x for x in self.tags if x['Key']=='odin_app_id'])==0:
            raise Exception("Key 'odin_app_id' not found")
        return self
    
    def create_job(self):
        """
        Description:
            | - Method to create lablieng job on SageMaker Ground Truth
        Return:
            | - (type: object {}) SageMaker GroundTrugh response object
        """
        client = boto3.client('sagemaker')
        sagemaker_response = client.create_labeling_job(
            LabelingJobName=self.job_name,
            LabelAttributeName='csa',
            InputConfig={
                'DataSource': {
                    'S3DataSource': {
                        'ManifestS3Uri': self.input_manifest_path
                    }
                },
                'DataAttributes': {
                    'ContentClassifiers': [
                        'FreeOfPersonallyIdentifiableInformation','FreeOfAdultContent'
                    ]
                }
            },
            OutputConfig={
                'S3OutputPath': self.output_manifest_path,
            },
            RoleArn = 'arn:aws:iam::716134864690:role/service-role/AmazonSageMaker-ExecutionRole-20181025T164256',
            HumanTaskConfig={
                'WorkteamArn': self.labeling_team_arn,
                'UiConfig': {
                    # template
                    'UiTemplateS3Uri': self.labeling_template_path,
                },
                # Pre-Processing Lambda
                'PreHumanTaskLambdaArn': self.preprocessing_labeling_lambda_arn,
                'TaskTitle': self.job_name,
                'TaskDescription': self.job_name,
                'NumberOfHumanWorkersPerDataObject': 1,
                'TaskTimeLimitInSeconds': self.task_time_limit,
                'TaskAvailabilityLifetimeInSeconds': self.job_availability_time,
                'MaxConcurrentTaskCount': 1000,
                'AnnotationConsolidationConfig': {
                    # Post-Processing Lambda
                    'AnnotationConsolidationLambdaArn': self.postprocessing_labeling_lambda_arn
                },
            },
            Tags=self.tags
        )
        
        return sagemaker_response
        
    def __property_validation(self, name):
        if not hasattr(self, name):
            raise Exception(f"Value for '{name}' not found")
        if getattr(self, name)==None:
            raise Exception(f"Value for '{name}' not found")
        if len(getattr(self, name))==0:
            raise Exception(f"Value for '{name}' not found")
       

