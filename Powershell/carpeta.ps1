Clear-Host
$Title = "Folder CarpetaProtegida"
$FolderName = "CarpetaProtegida"
$HiddenFolder = "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
$Password = "112481"

function Lock-Folder{
	Rename-Item $FolderName $HiddenFolder
	set-ItemProperty -Path $HiddenFolder -Name Attributes -Value ([System.IO.FileAttributes]::Hidden+[System.IO.FileAttributes]::System)
	write-host "Folder Locked"
}

function Unlock-Folder{
	$pass=Read-Host "Introduzca la constrasena para mostrar la CarpetaProtegida" -AsSecureString
    $BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($pass)
    $plainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)

	if ($plainPassword -eq $Password){
		set-ItemProperty -Path $HiddenFolder -Name Attributes -Value([system.io.FileAttributes]::Normal)
		Rename-Item $HiddenFolder $FolderName
		write-Host "Folder Unlock successfully"
	}else{
		write-host "Invalid password"
	}
}

function Create-Folder{
	New-Item -ItemType Directory -Name $FolderName
	write-host "CarpetaProtegida create successfully"
}

function confirm-Lock{
	$cho=Read-Host "Quiere ocultar la CarpetaProtegida?(S/N)"
	Switch ($cho.toUpper()){
		"S" {Lock-Folder}
		"N" {return}
		default {
			write-host "Invalid Choise"
			confirm-Lock
		}
	}
}

if (Test-Path $hiddenFolder){
	Unlock-Folder
}elseif (-not (Test-Path $FolderName)){
	create-Folder
}else {
	confirm-Lock
}

# Invoke-PS2EXE -InputFile "ruta\del\archivo.ps1" -OutputFile "ruta\del\archivo.exe"
# invoke-ps2exe -inputfile "ruta\del\archivo.ps1" -outputfile "ruta\del\archivo.exe" -iconfile "ruta\del\icono.ico" -noconsole
