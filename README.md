
# Implements Snap BI

I am trying to understand and apply Snap BI, especially for Virtual Account Transactions that are implemented in the Flask framework. This Snap BI can be checked at https://apidevportal.aspi-indonesia.or.id for details of its use.

The process being attempted is divided into two, namely the security process and apply service.

    1. Security
       This is used to get an access token which will later be used when running the service. In this process, I used some snap BI API
       1. Signature Auth
       2. Signature service
       3. Access Token B2B/B2BC
    2. Service
       There are many services provided in this documentation. However, currently, I am only trying to use one of the sub-services, which is the virtual account.
       1. Inquiry VA
    

![Logo](https://sinar.devajayantha.xyz/assets/images/bi/flow.png)

The starting stage is involves registration and requesting application testing. Perform authentication to obtain an access token to access the service. This is the process undertaken in using the Snap BI API.

    1. Signature Auth -> get signature auth
    2. Access Token B2B/B2BC (contoh B2B) (use signature auth) -> get access token 

Once the access token is obtained, I can then use each feature provided that I have the access token and the service signature. For example, if I want to access the service transfer VA inquiry.

    1. Signature Service (use access token, request body from service, and  endpoint url from service will excute) -> get signature service
    2. Transfer VA Inquiry (use access token, signature service, and the same request body ) -> response data service

So, the conclusion based on my understanding is that each time we use a service, we must obtain a service signature and an access token. The access token is typically generated once and remains valid until it expires. It can be used for multiple requests as long as it is still valid. On the other hand, the service signature (sometimes called an API signature or request signature) needs to be generated each time you want to access a specific service or make a request.


## API Reference

#### POST Auth Access Token

```http
  POST /api/v1/auth
```


#### POST apply VA transaction

```http
  POST /api/v1/auth/transaction
```
![Logo](https://sinar.devajayantha.xyz/assets/images/bi/apidoc.png)
I already add postman collections in project

### ThankYou


