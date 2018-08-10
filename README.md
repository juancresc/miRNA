1-

Lo primero es correr shorstack para buscar sRNA locis

nohup ./ShortStack/ShortStack --readfile  /media/crescentejuan/Data/MRCV/21dpiR1C.trimmed.fq.gz /media/crescentejuan/Data/MRCV/21dpiR1T.trimmed.fq.gz /media/crescentejuan/Data/MRCV/21dpiR3C.trimmed.fq.gz /media/crescentejuan/Data/MRCV/21dpiR3T.trimmed.fq.gz --genomefile  /media/crescentejuan/Data/TGAC/Triticum_aestivum.TGACv1.dna.toplevel.fa --outdir 21dpi_tgac &

Esto nos da 39.108 loci en total, y 28.844 los cuales DicerCall es distinto de 'N' (aquellos probablemente relacionados con RNAi). Vamos a usar esos 28k para los subsiguientes análisis.

De esos 28k, 139 son marcados por shortstack como miRNA=Y, o sea con suficiente evidencia para una anotación de-novo de miRNA. 

2-

De donde salen los sRNA loci? Cruzamos la anotación de esos 28k loci con genes y transposones. Se mapearon transposones al genoma de trigo de la base de datos Repbase, TREP y MITEs (estos últimos los buscamos con un programa nuestro) y se usan genes / regiones promotoras (2500 downstream de los genes).

Repbase 87
TREP 155
MITEs 2690
Genes 4853
Promotores 9394

3- 

Se arma una tabla con los read counts de esos 28k de la forma:

locus_name, counts_21dpiR1C, counts_21dpiR1T, counts_21dpiR3C, counts_21dpiR3T

4-

Se corre DESeq2 con esos 28k counts. Eso nos da 43 locis DE. De esos 43, 37 tienen log2FoldChange positivo y 6 negativos. La mayoria están sobreexpresados.

De los 43 loci DE, hay 3 que son miRNA=Y según shorstack:

Cluster_12900
Cluster_14161
Cluster_36675


TODO de aca en adelante

5- 

De donde salen esos 43 locis DE? Se corre el mismo script que en 2) y se obtiene

Repbase 0
TREP 0
MITEs 1
Genes 12
Promotores 7

6- 

Genes DE cercanos a clusters de sRNA DE. Se toman los clusters DE y se cruzan con los genes DE cercanos (1500 pb). Además vemos si estan up/down stream de los mismos. Nos da lo siguiente:

7-

Targets: Buscamos de los clusters DE, los genes DE que pueden ser targets.


8- 

Anotación: 