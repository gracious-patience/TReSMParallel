

import torch
import torchvision
import torchvision.transforms.functional as F
import folders


class DataLoader(object):
	"""
	Dataset class for IQA databases
	"""

	def __init__(self, dataset, path, img_indx, patch_size, patch_num, seed, k, batch_size=1, istrain=True):

		self.batch_size = batch_size
		self.istrain = istrain

		if (dataset == 'live') | (dataset == 'csiq') | (dataset == 'sly_csiq') | (dataset == 'tid2013') | (dataset == 'sly_tid2013') | (dataset == 'clive')| (dataset == 'kadid10k') | (dataset == 'sly_kadid10k') | (dataset == 'pipal') | (dataset == 'sly_pipal'):
			if istrain:
				transforms = torchvision.transforms.Compose([
					torchvision.transforms.RandomHorizontalFlip(),
					torchvision.transforms.RandomVerticalFlip(),
					torchvision.transforms.RandomCrop(size=patch_size),
					torchvision.transforms.ToTensor(),
					torchvision.transforms.Normalize(mean=(0.485, 0.456, 0.406),
													 std=(0.229, 0.224, 0.225))
				])
			else:
				transforms = torchvision.transforms.Compose([
					torchvision.transforms.RandomCrop(size=patch_size),
					torchvision.transforms.ToTensor(),
					torchvision.transforms.Normalize(mean=(0.485, 0.456, 0.406),
													 std=(0.229, 0.224, 0.225))
				])
		elif dataset == 'koniq' or dataset == 'big_koniq':
			if istrain:
				transforms = torchvision.transforms.Compose([
					torchvision.transforms.RandomHorizontalFlip(),
					torchvision.transforms.RandomVerticalFlip(),
					torchvision.transforms.RandomCrop(size=patch_size),
					torchvision.transforms.ToTensor(),
					torchvision.transforms.Normalize(mean=(0.485, 0.456, 0.406),
													 std=(0.229, 0.224, 0.225))])
			else:
				transforms = torchvision.transforms.Compose([
					torchvision.transforms.RandomCrop(size=patch_size),
					torchvision.transforms.ToTensor(),
					torchvision.transforms.Normalize(mean=(0.485, 0.456, 0.406),
													 std=(0.229, 0.224, 0.225))])
		elif dataset == 'spaq':
			if istrain:
				transforms = torchvision.transforms.Compose([
					torchvision.transforms.RandomHorizontalFlip(),
					torchvision.transforms.RandomVerticalFlip(),
					torchvision.transforms.RandomCrop(size=patch_size),
					torchvision.transforms.ToTensor(),
					torchvision.transforms.Normalize(mean=(0.485, 0.456, 0.406),
													 std=(0.229, 0.224, 0.225))])
			else:
				transforms = torchvision.transforms.Compose([
					torchvision.transforms.RandomCrop(size=patch_size),
					torchvision.transforms.ToTensor(),
					torchvision.transforms.Normalize(mean=(0.485, 0.456, 0.406),
														std=(0.229, 0.224, 0.225))])
		elif dataset == 'biq':
			if istrain:
				transforms = torchvision.transforms.Compose([
					torchvision.transforms.RandomHorizontalFlip(),
					torchvision.transforms.RandomVerticalFlip(),
					torchvision.transforms.RandomCrop(size=patch_size),
					torchvision.transforms.ToTensor(),
					torchvision.transforms.Normalize(mean=(0.485, 0.456, 0.406),
													 std=(0.229, 0.224, 0.225))])
			else:
				transforms = torchvision.transforms.Compose([
					torchvision.transforms.RandomCrop(size=patch_size),
					torchvision.transforms.ToTensor(),
					torchvision.transforms.Normalize(mean=(0.485, 0.456, 0.406),
														std=(0.229, 0.224, 0.225))])

		elif dataset == 'fblive':
			if istrain:
				transforms = torchvision.transforms.Compose([
					torchvision.transforms.Resize((512, 512)),
					torchvision.transforms.RandomHorizontalFlip(),
					torchvision.transforms.RandomVerticalFlip(),
					torchvision.transforms.RandomCrop(size=patch_size),
					torchvision.transforms.ToTensor(),
					torchvision.transforms.Normalize(mean=(0.485, 0.456, 0.406),
													 std=(0.229, 0.224, 0.225))])
			else:
				transforms = torchvision.transforms.Compose([
					torchvision.transforms.Resize((512, 512)),
					torchvision.transforms.RandomCrop(size=patch_size),
					torchvision.transforms.ToTensor(),
					torchvision.transforms.Normalize(mean=(0.485, 0.456, 0.406),
													 std=(0.229, 0.224, 0.225))])

		if dataset == 'live':
			self.data = folders.LIVEFolder(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num)
		elif dataset == 'clive':
			self.data = folders.LIVEChallengeFolder(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num, istrain=istrain, k=k)
		elif dataset == 'csiq':
			self.data = folders.CSIQFolder(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num, istrain=istrain, k=k)
		elif dataset == 'sly_csiq':
			self.data = folders.SlyCSIQFolder(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num, istrain=istrain, k=k)
		elif dataset == 'koniq':
			self.data = folders.Koniq_10kFolder(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num, istrain=istrain, k=k)
		elif dataset == 'big_koniq':
			self.data = folders.BigKoniq_10kFolder(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num)
		elif dataset == 'fblive':
			self.data = folders.FBLIVEFolder(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num)
		elif dataset == 'tid2013':
			self.data = folders.TID2013Folder(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num, istrain=istrain, k=k)
		elif dataset == 'sly_tid2013':
			self.data = folders.SlyTID2013Folder(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num, istrain=istrain, k=k)
		elif dataset == 'kadid10k':
			self.data = folders.Kadid10k(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num, istrain=istrain, k=k)
		elif dataset == 'sly_kadid10k':
			self.data = folders.SlyKadid10k(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num, istrain=istrain, k=k)				
		elif dataset == 'spaq':
			self.data = folders.SpaqFolder(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num, istrain=istrain, k=k)	
		elif dataset == 'biq':
			self.data = folders.BiqFolder(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num, istrain=istrain, k=k)
		elif dataset == 'pipal':
			self.data = folders.PipalFolder(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num, istrain=istrain, k=k)
		elif dataset == 'sly_pipal':
			self.data = folders.SlyPipalFolder(
				root=path, seed=seed, index=img_indx, transform=transforms, patch_num=patch_num, istrain=istrain, k=k)

	def get_data(self):
		if self.istrain:
			dataloader = torch.utils.data.DataLoader(
				self.data, batch_size=self.batch_size, shuffle=True, num_workers=32)
		else:
			dataloader = torch.utils.data.DataLoader(
				self.data, batch_size=self.batch_size, shuffle=False, num_workers=32)
		return dataloader
