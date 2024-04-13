"""Lists: An ordered collection of items used when you need to work with a collection of related items"""
#Create a list of AWS services

def main():
    aws_services = ["ec2", "s3", "lambda", "sns", "sqs", "vpc"]
    #print aws services
    print(f"The AWS services : {aws_services}")

    #Print First item 
    first_service = aws_services[0]
    print(f"First Service : {first_service}")

    #Print last service
    last_service = aws_services[-1]
    print(f"Last Service : {last_service}")

    #modify the last service in the list
    aws_services[-1] = "DynamoDB"
    print(f"Modified Services : {aws_services}")

    #add a new service to list
    aws_services.append("APIGateway")
    print(f"New Services: {aws_services}")

    #Remove s3 from list
    aws_services.pop(1)
    print(f"New services after removing s3 : {aws_services}")

    #slice the list to get services from index 1 to 3(inclusive of 1 and exclusive of 3)
    sliced_list = aws_services[1:3]
    print(f"Sliced list : {sliced_list}")

    #Find the length of the list
    Len=len(aws_services)
    print(f"Length of list : {Len}")

if __name__ == '__main__':
    main()