a
    �m�a�  �                   @   s>   d dl mZ d dlmZ ddlmZmZ G dd� dej�ZdS )�    )�fields)�serializers�   )�PQR�PersonaSoportec                   @   s,   e Zd ZG dd� d�ZG dd� dej�ZdS )�PersonaSoporteSerializerc                   @   s   e Zd ZeZdZdS )zPersonaSoporteSerializer.Meta�__all__N)�__name__�
__module__�__qualname__r   �modelr   � r   r   �(C:\Desarrollo\ms1\soporte\serializers.py�Meta   s   r   c                   @   s   e Zd ZG dd� d�ZdS )z&PersonaSoporteSerializer.PQRSerializerc                   @   s   e Zd ZeZg d�ZdS )z+PersonaSoporteSerializer.PQRSerializer.Meta)�persona_soporte�estado�
comentarioN)r	   r
   r   r   r   r   r   r   r   r   r      s   r   N)r	   r
   r   r   r   r   r   r   �PQRSerializer   s   r   N)r	   r
   r   r   r   �ModelSerializerr   r   r   r   r   r      s   r   N)	�django.db.modelsr   �rest_frameworkr   �modelsr   r   r   r   r   r   r   r   �<module>   s   