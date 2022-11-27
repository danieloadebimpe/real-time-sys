import { Button, Card, CardContent, TextField, Typography } from "@mui/material";
import  { CardActions, Grid } from "@mui/material";
import { ethers } from "ethers"; 
import { Consumer_Contract } from "./Web3";
import { useState, useEffect } from "react";
import { makeStyles } from "@mui/styles";


const Oracle = () => {

    const [data, setData] = useState("");

    const getData = async () => {
        const get_data = await Consumer_Contract.data();
        setData(get_data.toNumber());
        console.log("the temperature of the raspberry pi cpu is: ", get_data.toNumber());
    }


    const request = async () => {
        console.log("getting data");
        const request_data = await Consumer_Contract.requestData();

    }

    const useStyles = makeStyles({

        root: {
            backgroundColor: "forestgreen",
            color: "white"
    
        },
    
        button: {
            color: "black",
            backgroundColor: "orange"
    
        }
    
    });

    const classes = useStyles();

    return (
        <div>
            <Grid container justify="center" spacing={4} />
            <Grid item xs={6} sm={6} md={4}>
            <Card sx={{maxWidth: 345}} className={classes.root}>
                <CardContent>
                    <Typography gutterBottom variant="h5" component="div">
                        Request Data
                        <p> this will send a request to the api you set in the contract</p>
                    </Typography>
                </CardContent>
                <Button
                className={classes.button}
                variant="contained"
                onClick={request}
                > request data 
                </Button>
            </Card>
        </Grid>
        <br></br>
        <Grid container justify="center" spacing={4} />
            <Grid item xs={6} sm={6} md={4} >
                <Card sx={{maxWidth: 345}} className={classes.root}>
                    <CardContent>
                        <Typography gutterBottom variant="h5" component="div">
                            Fetched data
                            <p>this is the variable you got after requesting data</p>
                            <br></br>
                            {data}
                        </Typography>
                        {/* <Typography variant="body2" color="text.secondary" >
                        </Typography> */}
                    </CardContent>
                    <Button
                        className={classes.button}
                        variant="contained"
                        onClick={getData}
                        > get
                    </Button>
                </Card>
            </Grid>
        </div>
    )

}


export default Oracle;