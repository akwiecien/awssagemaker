import pytest
from sagemaker_groundtruth.sagemaker_groundtruth_internal import SageMakerGroundTruthInternal


def test_instance_return():
    instance = SageMakerGroundTruthInternal.get_builder()
    assert instance != None   
    assert isinstance(instance, SageMakerGroundTruthInternal)

def test_exception_not_found_raises():
    instance = SageMakerGroundTruthInternal.get_builder()
    with pytest.raises(Exception) as excinfo:   
        instance.build()
    assert str(excinfo.value) == "Value for 'job_name' not found"

@pytest.fixture()
def instance_object():
    return SageMakerGroundTruthInternal.get_builder() \
        .with_job_name("job_name") \
        .with_labeling_team("labeling_team") \
        .with_preprocessing_lambda("lambda") \
        .with_postprocessing_lambda("lambda") \
        .with_attribute_name("attr") \
        .with_input_manifest_path("path") \
        .with_output_manifest_path("path") \
        .with_labeling_template_path("path") \
        .with_task_time_limit("limit") \
        .with_job_availability_time("limit")

def test_exception_tag_wrong_type_raises(instance_object):
    with pytest.raises(Exception) as excinfo:   
        instance_object.with_tags({}).build()
    assert str(excinfo.value) == "Value for 'tags' not found"    

def test_exception_tag_empty_list_raises(instance_object):
    with pytest.raises(Exception) as excinfo:   
        instance_object.with_tags([]).build()
    assert str(excinfo.value) == "Value for 'tags' not found"
    
def test_exception_tag_missing_odin_app_id_raises(instance_object):
    with pytest.raises(Exception) as excinfo:   
        instance_object.with_tags([{'Key':'fake_key','Value':'fake_value'}]).build()
    assert str(excinfo.value) == "Key 'odin_app_id' not found"
    
def test_exception_tag_missing_odin_app_id_raises(instance_object):
    instance = instance_object.with_tags([{'Key':'odin_app_id','Value':'odin_value'}]).build()
    assert instance != None   
    assert isinstance(instance, SageMakerGroundTruthInternal)


def test_excpetion_if_properties_are_wrong_raises(instance_object):
    with pytest.raises(Exception) as excinfo:   
        instance_object.with_tags([{'Key':'odin_app_id','Value':'odin_value'}]).build().create_job()


# for debugging
if __name__ == "__main__":
    pytest.main(["tests/unit/test_sagemakergroundtruth.py", "-s"])