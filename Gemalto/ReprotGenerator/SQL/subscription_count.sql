set pagesize 0 feedback off verify off heading off echo off

select count(*) from RHS_HISTORY where  
	C_ENDING_STATUS='&5' and 
	c_mno='&1' and 
	c_service_name='&4' 
	and d_timestamp between 
	to_Date ('&2', 'YYYY-MM-DD"T"HH24:MI:SS') and 
	to_Date ('&3', 'YYYY-MM-DD"T"HH24:MI:SS');
