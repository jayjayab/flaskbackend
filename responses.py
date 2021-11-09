from flask import Response, json

def response(output):
    if 'Error' in output:
        return Response(response=json.dumps({"Response": output}),
                        status=400,
                        mimetype='application/json')
    else:
        return Response(response=json.dumps(output, sort_keys=False),
                        status=200,
                        mimetype='application/json')


def incomplete_details_response():
    return Response(response=json.dumps({"Response": "Please provide all the details"}),
                    status=200,
                    mimetype='application/json')
