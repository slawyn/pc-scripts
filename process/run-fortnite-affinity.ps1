$fn=Start-Process -FilePath "C:\Program Files\Epic Games\Fortnite\FortniteGame\Binaries\Win64\FortniteClient-Win64-Shipping.exe" -PassThru
$fn.ProcessorAffinity = [int]0x5550
$fn.PriorityClass = 'ABOVENORMAL'

while(1){
	$fn = Get-Process FortniteClient-Win64-Shipping
	if(($fn -eq $null) -or ($fn.HasExited)){
		break
	}
	$fn.ProcessorAffinity = [int]0x5550
	$fn.PriorityClass = 'ABOVENORMAL'
	sleep 180

}

