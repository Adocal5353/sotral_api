from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
class BusList(APIView):
    def get(self, request, format=None):  # Affiche livre
        buss = Bus.objects.all()
        serializer = BusSerializer(buss, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):  # Créer livre
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BusDetail(APIView):
    def get_object(self, pk):
        try:
            return Bus.objects.get(pk)
        except Bus.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bus = self.get_object(pk)
        serializer = BusSerializer(bus)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  # MAJ de livre
        bus = self.get_object(pk)
        serializer = BusSerializer(bus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  # Supprime livre
        bus = self.get_object(pk)
        bus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            instance = Bus.objects.get(pk=pk)
        except Bus.DoesNotExist:
            return Response({"error": "Ressource non trouvée"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BusSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LigneList(APIView):
    def get(self, request, format=None):  # Affiche livre
        lignes = Ligne.objects.all()
        serializer = LigneSerializer(lignes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):  # Créer livre
        serializer = LigneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LigneDetail(APIView):
    def get_object(self, pk):
        try:
            return Ligne.objects.get(pk)
        except Ligne.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ligne = self.get_object(pk)
        serializer = LigneSerializer(ligne)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  # MAJ de livre
        ligne = self.get_object(pk)
        serializer = LigneSerializer(ligne, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  # Supprime livre
        ligne = self.get_object(pk)
        ligne.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            instance = Ligne.objects.get(pk=pk)
        except Ligne.DoesNotExist:
            return Response({"error": "Ressource non trouvée"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LigneSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SectionList(APIView):
    def get(self, request, format=None):  # Affiche livre
        sections = Section.objects.all()
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):  # Créer livre
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SectionDetail(APIView):
    def get_object(self, pk):
        try:
            return Section.objects.get(pk)
        except Section.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        section = self.get_object(pk)
        serializer = SectionSerializer(section)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  # MAJ de livre
        section = self.get_object(pk)
        serializer = SectionSerializer(section, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  # Supprime livre
        section = self.get_object(pk)
        section.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            instance = Section.objects.get(pk=pk)
        except Section.DoesNotExist:
            return Response({"error": "Ressource non trouvée"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SectionSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UtilisateurList(APIView):
    def get(self, request, format=None):  # Affiche livre
        utilisateurs = Utilisateur.objects.all()
        serializer = UtilisateurSerializer(utilisateurs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):  # Créer livre
        serializer = UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UtilisateurDetail(APIView):
    def get_object(self, pk):
        try:
            return Utilisateur.objects.get(pk)
        except Utilisateur.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        utilisateur = self.get_object(pk)
        serializer = UtilisateurSerializer(utilisateur)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  # MAJ de livre
        utilisateur = self.get_object(pk)
        serializer = UtilisateurSerializer(utilisateur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  # Supprime livre
        utilisateur = self.get_object(pk)
        utilisateur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            instance = Utilisateur.objects.get(pk=pk)
        except Utilisateur.DoesNotExist:
            return Response({"error": "Ressource non trouvée"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UtilisateurSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoyageList(APIView):
    def get(self, request, format=None):  # Affiche livre
        voyages = Voyager.objects.all()
        serializer = VoyageSerializer(voyages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):  # Créer livre
        serializer = VoyageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoyageDetail(APIView):
    def get_object(self, pk):
        try:
            return Voyager.objects.get(pk)
        except Voyager.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        voyage = self.get_object(pk)
        serializer = VoyageSerializer(voyage)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  # MAJ de livre
        voyage = self.get_object(pk)
        serializer = VoyageSerializer(voyage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  # Supprime livre
        voyage = self.get_object(pk)
        voyage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            instance = Voyager.objects.get(pk=pk)
        except Voyager.DoesNotExist:
            return Response({"error": "Ressource non trouvée"}, status=status.HTTP_404_NOT_FOUND)

        serializer = VoyageSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TRANSACTION
@api_view(['POST'])
def credit_account(request):
    if request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            tarif_price = serializer.validated_data['tarif_price']

            try:
                utilisateur = Utilisateur.objects.get(idUser=user_id)
            except Utilisateur.DoesNotExist:
                return Response({"message": "Utilisateur non trouvé"}, status=404)

            # Créditer le compte de l'utilisateur
            utilisateur.compte += tarif_price
            utilisateur.save()

            return Response({"message": "Transaction réussie", "compte": utilisateur.compte})
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def debit_account(request):
    if request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            tarif_price = serializer.validated_data['tarif_price']

            try:
                utilisateur = Utilisateur.objects.get(idUser=user_id)
            except Utilisateur.DoesNotExist:
                return Response({"message": "Utilisateur non trouvé"}, status=404)

            if utilisateur.compte < tarif_price:
                return Response({"message": "Solde insuffisant"}, status=400)

            # Débiter le compte de l'utilisateur
            utilisateur.compte -= tarif_price
            utilisateur.save()

            return Response({"message": "Débit réussi", "compte": utilisateur.compte})
        return Response(serializer.errors, status=400)



class TarifList(APIView):
    def get(self, request, format=None):  # Affiche livre
        tarifs = Tarif.objects.all()
        serializer = TarifSerializer(tarifs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):  # Créer livre
        serializer = TarifSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Tarif
class TarifDetail(APIView):
    def get_object(self, pk):
        try:
            return Tarif.objects.get(pk)
        except Tarif.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tarif = self.get_object(pk)
        serializer = TarifSerializer(tarif)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  # MAJ de livre
        tarif = self.get_object(pk)
        serializer = TarifSerializer(tarif, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  # Supprime livre
        tarif = self.get_object(pk)
        tarif.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            instance = Tarif.objects.get(pk=pk)
        except Tarif.DoesNotExist:
            return Response({"error": "Ressource non trouvée"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TarifSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
