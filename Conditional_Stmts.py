#Determine the appropriate AWS service based on the user requirement
def main():
    #Define user requirement
    user_req = "Serverless_Computing"

    if user_req == "File_Storage":
        aws_service = "S3"
    elif user_req == "Virtual_Server":
        aws_service = "EC2"
    elif user_req == "Serverless_Computing":
        aws_service = "Lambda"
    else:
        aws_service = "Unknown"

    #Print the recommended AWS service based on user_requirement
    #check if the service is not known
    if user_req == "Unknown":
        print(f"The AWS service required is {aws_service}")
    else:
        print(f"The AWS service required is {aws_service}")

if __name__ == '__main__':
    main()