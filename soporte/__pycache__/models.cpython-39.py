a
    #�a#  �                   @   s@   d dl mZ d dlmZ G dd� dej�ZG dd� dej�ZdS )�    )�models)�SET_NULLc                   @   s2   e Zd Zejdd�Zejddd�Zejdd�Z	dS )�PersonaSoporte�@   ��
max_lengthT)�null�blank)�defaultN)
�__name__�
__module__�__qualname__r   �	CharFieldZnombre�IntegerFieldZedad�BooleanFieldZactivo� r   r   �#C:\Desarrollo\ms1\soporte\models.pyr      s   r   c                   @   s>   e Zd Zejeejdd�Zejdd�Z	ej
dd�Ze�� ZdS )�PQRT)�	on_deleter   �    r   )r	   N)r   r   r   r   �
ForeignKeyr   r   Zpersona_soporter   Zestado�	TextFieldZ
comentario�	DateFieldZcreacionr   r   r   r   r      s   r   N)�	django.dbr   �django.db.models.deletionr   �Modelr   r   r   r   r   r   �<module>   s   