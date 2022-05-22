from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''Permite usuario editar su perfil'''
    def has_object_permission(self, request, view, obj):
        '''chequeamos si usuario esta intentando editar su propio perfil'''
        if request.method in permissions.SAFE_METHODS:
            return True
        '''chequeamo si el objeto que estan actualizando tiene un march con el objeto
        del request original del usuario autenticado que ellos tienen'''
        return obj.id == request.user.id