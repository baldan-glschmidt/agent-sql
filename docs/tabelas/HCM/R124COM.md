# R124COM

## Descrição

Colaborador - Comunicação

---

## Resumo

- Campos: 15
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador Candidato |
| DatCom | Date | Não | Data da comunicação com o Candidato |
| HorCom | Number(005,0) | Não | Hora da comunicação com o Candidato |
| EnvRec | Number(001,0) | Sim | Tipo de comunicação com o Candidato: Envio ou Recebimento |
| EndNum | String(255) | Sim | Endereço/Número utilizado para a comunicação |
| AssCom | String(100) | Sim | Assunto da comunicação com o Candidato |
| TxtCom | String(40000) | Sim | Texto da comunicação com o Candidato |
| DthEma | Number(014,6) | Sim | Data/Hora que o e-mail for enviado |
| CodUsu | Number(009,0) | Sim | Usuário responsável pelo último registro da comunicação como o Candidato |
| DthMod | Number(014,6) | Sim | Data/Hora da última modificação no registro da comunicação como o Candidato |
| CodRqu | Number(009,0) | Sim | Código da Requisição que a comunicação está vinculada |
| TipCom | Number(001,0) | Sim | Tipo de comunicação realizada com o Candidato |
| CodEEl | Number(004,0) | Sim | Código do tipo de endereço eletrônico |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatCom
- HorCom

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
