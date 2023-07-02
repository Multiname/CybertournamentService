import {Typography} from '@mui/material'
import Button from '@mui/material/Button';
import Toolbar from '@mui/material/Toolbar';
import AppBar from '@mui/material/AppBar';
import IconButton from '@mui/material/IconButton';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import CottageOutlinedIcon from '@mui/icons-material/CottageOutlined';
import { MAIN_PAGE_ROUTE, RATING_ROUTE, TOURNAMENTS_ROUTE, COMMANDS_ROUTE } from '../consts';
import {useNavigate} from 'react-router-dom'


const Navbar = () => {

    const history = useNavigate()

    return (
        <AppBar position="static" color="secondary">
            <Toolbar>
                <IconButton edge="start" color="inherit" aria-label="menu" onClick={() => history(MAIN_PAGE_ROUTE)}>
                    <CottageOutlinedIcon fontSize='large'/>
                </IconButton>
                <IconButton edge="start" color="inherit" aria-label="menu" sx={{ml: 3}}>
                    <AccountCircleIcon/>
                    <Typography variant="h6">
                    Вход
                </Typography>
                </IconButton>
                <Button color="inherit" sx={{ml: 3}} onClick={() => history(TOURNAMENTS_ROUTE)}>Турниры</Button>
                <Button color="inherit" sx={{ml: 3}} onClick={() => history(COMMANDS_ROUTE)}>Команды</Button>
                <Button color="inherit" sx={{ml: 3}} onClick={() => history(RATING_ROUTE)}>Рейтинги</Button>
            </Toolbar>
        </AppBar>
    )
}

export default Navbar;