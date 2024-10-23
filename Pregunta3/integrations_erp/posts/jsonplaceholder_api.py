import requests
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'integrations_erp.settings')
application = get_wsgi_application()

from posts.models import FactPosts, DimUsers, DimPosts, DimAddresses, DimCompanies
from django.conf import settings

def call_api_jsonplaceholder(url_user, url_post):
    try:
        response_user = requests.get(url_user)
        response_post = requests.get(url_post)
        if response_user.status_code and response_post.status_code == 200:
            data_user = response_user.json()
            data_post = response_post.json()
            post_dict = {}
            for post in data_post:
                user_id = post['userId']
                if user_id not in post_dict:
                    post_dict[user_id] = []
                post_dict[user_id].append(post)
            
            for user_data in data_user:
                user_id = user_data['id']
                
                # print(user_data['address'])
                # print(post_dict)
                user = create_user(user_data)
                # print('YA SE CREARON LOS USERS')
                
                for post in post_dict.get(user_id, []):
                    # print(f'AQUI ESTA EL POST QUE DEBERÍA IR AL USER {post}')
                    post_obj = create_post(post)
                    
                    create_factPost(user, post_obj)
                    
            print('Se han creado FactPosts correctamente')
        else:
            print(f"Ha fallado la respuesta con el siguiente código: {response_user.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Ha ocurrido un error: {e}")


def create_address(address_data):
    try:
        address = DimAddresses.objects.update_or_create(
            street=address_data['street'],
            suite=address_data['suite'],
            city=address_data['city'],
            zipcode=address_data['zipcode']
        )
        return address
    except Exception as e:
        print(f'Ocurrió el siguiente error: {e}')

def create_company(company_data):
    try: 
        company = DimCompanies.objects.update_or_create(
            name=company_data['name'],
            catchPhrase=company_data['catchPhrase'],
            bs=company_data['bs']
        )
        return company
    except Exception as e:
        print(f'Ocurrió el siguiente error: {e}')


def create_user(user_data):
    try:
        address = create_address(user_data['address'])
        company = create_company(user_data['company'])
        user = DimUsers.objects.update_or_create(
            username=user_data['username'],
            name = user_data['name'],
            email = user_data['email'],
            phone = user_data['phone'],
            website = user_data['website'],
            address = address[0],
            company = company[0],
        )
        return user
    except Exception as e:
        print(f'Ocurrió el siguiente error: {e}')

def create_post(post_data):
    try:
        post = DimPosts.objects.update_or_create(
            userId = post_data['userId'],
            title = post_data['title'],
            body = post_data['body']
        )
        return post
    except Exception as e:
        print(f'Ocurrió el siguiente error: {e}')

def create_factPost(user, post):
    try: 
        factPost = FactPosts.objects.create(
            users=user[0],
            posts=post[0],
        )
        return factPost
    except Exception as e:
        print(f'Ocurrió el siguiente error: {e}')


url_user = 'https://jsonplaceholder.typicode.com/users'
url_post = 'https://jsonplaceholder.typicode.com/posts'
call_api_jsonplaceholder(url_user, url_post)