    UPDATE [DataWarehouse].[dbo].[Plant_BR401101_Dados]
  SET 
      [kWhPerNm3]= IIF([ProducaoLiquidaLTotal_M3]>0,dbo.GREATEST(([Energia Light]/[ProducaoLiquidaLTotal_M3]),0),0),
      [TonsPerMWh] = IIF([Energia Light]>0,(COALESCE((([ProducaoLiquidaLOX_M3]*1.4286+[ProducaoLiquidaLIN_M3]*1.2502+[ProducaoLiquidaLAR_M3]*1.7836)/1.0772),0)/COALESCE([Energia Light],0),0)),
      [O2Recovery] = IIF([AirToCB]>0,dbo.GREATEST(([ProducaoLiquidaLOX_M3] + [ConsumoGerdau_Nm3_GOX_MM])/([AirToCB]*0.2095),0),0),
      [ArRecovery] = IIF([AirToCB]>0,dbo.GREATEST([ProducaoLiquidaLAR_M3]/([AirToCB]*0.00934),0),0),
      [Spezi]  =  IIF([Energia Light]>0,dbo.GREATEST(([ProducaoLiquidaLTotal_M3] / [Energia Light]),0),0)