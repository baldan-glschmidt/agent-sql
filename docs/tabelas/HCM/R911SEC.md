# R911SEC

## Descrição

Controle de conexões

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumSec | Number(014,0) | Não | Número interno |
| DatTim | Number(014,6) | Sim | Data do inicio da conexão |
| ComNam | String(060) | Sim | Nome da estação de trabalho |
| UsrNam | String(060) | Sim | Nome do usuário da rede |
| AppNam | String(255) | Sim | Caminho e nome da aplicação |
| AppUsr | String(060) | Sim | Usuário da aplicação |
| IDInst | Number(003,0) | Sim | ID da instância do banco |
| AdmMsg | Number(003,0) | Sim | Mensagens Administrativas |
| AppKnd | Number(001,0) | Sim | Forma de Acesso |

---

## Chave Primária

- NumSec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
