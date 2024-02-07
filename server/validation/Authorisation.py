# import functools
# from flask import jsonify,request,g

# import os
# import jwt
# secretKey = os.getenv('SECRET_KEY')


# def login_required(func):
#     @functools.wraps(func)
#     def checkJWT(*args, **kwargs):
#         # Do something before

#         auth=False
#         jwtToken=request.headers.get('Authorization') #Bearer <JWT>

#         print(jwtToken)
#         if jwtToken:
#             jwtToken=jwtToken.split(" ")[1]#JWT value

#             try:
#                 payload=jwt.decode(jwtToken, secretKey,algorithms=['HS256'])
#                 auth=True

#                 g.role=payload["role"]
#                 g.userid=payload["userid"]

#             except jwt.InvalidSignatureError as err:            
#                 print(err)
#             except jwt.ExpiredSignatureError as err:
#                 print(err)
#             except jwt.InvalidTokenError as err:
#                 print(err)

#         if auth==True:
#             value = func(*args, **kwargs)
#             # Do something after
#             return value

#         else:
#             return jsonify({"Message":"JWT Error"}),500

#     return checkJWT