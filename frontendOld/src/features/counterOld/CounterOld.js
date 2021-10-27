import React,{useState} from "react";
import styled from 'styled-components';
import Button from '@mui/material/Button';
import MailIcon from '@mui/icons-material/Mail';
import Badge from '@mui/material/Badge';
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';
import Stack from '@mui/material/Stack';


export default function CounterOld(){
    const [count, setCount] = useState(0) //저장장소와 쓰기 getter,setter 

    return(<CounterDiv>
        {count == 0 && <Stack sx={{ width: '300px' , 'margin': '0 auto' }} spacing={2}>
        <Alert severity="warning">
            <AlertTitle>Warning</AlertTitle>
            <strong>메일이 없습니다.</strong>
        </Alert>
        </Stack>}
        
        <Badge badgeContent={count >= 0 ? count : setCount(0)} color="secondary" style={{marginBottom:'20px'}}>
        <MailIcon color="action" />
        </Badge>
        <br/>
        <Button variant="outlined" onClick={() => setCount(count+1)}>Add</Button>
        <SpanStyle/>
        <Button variant="outlined" onClick={() => setCount(count-1)}>del</Button>
    </CounterDiv>)
}

const CounterDiv = styled.div`text-align: center; padding: 20em;`
const SpanStyle = styled.span`margin: 10px;`