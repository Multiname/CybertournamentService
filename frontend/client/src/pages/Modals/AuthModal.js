import Modal from "@mui/material/Modal";
import Box  from "@mui/material/Box";
import { Button, InputLabel, Typography, Input, FormHelperText} from "@mui/material";
import FormControl from "@mui/material/FormControl";


const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    pt: 2,
    px: 4,
    pb: 3,
};


const AuthModal = ({open, handleClose}) => {
    return(
        <Modal
            open={open}
            onClose={handleClose}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description"
        >
            <Box sx={style}>
                <Typography id="modal-modal-title" variant="h6" component="h2">
                    Авторизация
                </Typography>
                <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                    <FormControl sx={{width: 400}}>
                        {/* <InputLabel>Email адрес</InputLabel> */}
                        <Input id="email" type="email" placeholder="Введите Email"/>

                        {/* <InputLabel>Пароль</InputLabel> */}
                        <Input id="password" type="password" placeholder="Введите пароль"/>

                        <Button color="secondary">Войти</Button>
                        <Button color="secondary" onClick={handleClose}>Закрыть</Button>
                    </FormControl>
                </Typography>
            </Box>
        </Modal>
    )
}

export default AuthModal;