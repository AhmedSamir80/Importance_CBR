
CalculateAccuracy <- function(path1,path2)
{
  Files_Names = c('P0.csv','P1.csv','P2.csv','P3.csv','P4.csv','P5.csv','P6.csv','P7.csv','P8.csv','P9.csv')
  for (File_Name in Files_Names) 
  {
    print(paste("File name is",File_Name))
    TotalFileNAme=paste(path1,File_Name,sep='')
    df1 <- read.csv(file=TotalFileNAme, header=TRUE, sep=",")
    TotalFileNAme=paste(path2,File_Name,sep='')
    df2 <- read.csv(file=TotalFileNAme, header=TRUE, sep=",")
    mergedDF = (merge.data.frame(df1,df2,by.x = 'ID1',by.y = 'ID1')) 
    
    Diffrence = mergedDF[mergedDF$ID2.y!=mergedDF$ID2.x,'ID1']
    print("Diffrence ids are")
    print(Diffrence)
    print("Accuracy = ")
    print(1-(length(Diffrence)/nrow(df1)))
    
  }
  
}


