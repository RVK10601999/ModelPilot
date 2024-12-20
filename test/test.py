import streamlit as st
import pickle
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def export_model_to_s3(model):
    st.title("Model Exporting to S3")
    
    # Input for S3 details
    bucket_name = st.text_input("S3 Bucket Name:", "")
    file_name = st.text_input("File Name in S3 (e.g., `model.pkl`):", "model.pkl")
    
    if st.button("Save Model to S3"):
        if bucket_name and file_name:
            try:
                # Serialize the model to a binary stream
                model_data = pickle.dumps(model)
                
                # Connect to S3 and upload the model
                s3 = boto3.client("s3")
                s3.put_object(Bucket=bucket_name, Key=file_name, Body=model_data)
                
                st.success(f"Model successfully saved to s3://{bucket_name}/{file_name}")
            except NoCredentialsError:
                st.error("AWS credentials not found. Ensure the EC2 instance has an IAM role with S3 write permissions.")
            except PartialCredentialsError as e:
                st.error(f"Credential issue: {e}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please provide both bucket name and file name.")

# Example usage
if __name__ == "__main__":
    # Replace 'model' with your trained ML model
    model = {"example_model": "This is a placeholder for your trained model"}
    export_model_to_s3(model)
