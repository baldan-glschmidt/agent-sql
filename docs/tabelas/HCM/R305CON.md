# R305CON

## Descrição

e-Sfinge Online - Status - Concursos/Processos Seletivos

---

## Resumo

- Campos: 19
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumEdi | String(016) | Não | Número do edital de concurso |
| SeqReg | Number(009,0) | Não | Sequência |
| DatRef | Date | Sim | Data de referência do registro |
| StaEnv | String(001) | Sim | Status do Envio |
| JusCan | String(500) | Sim | Justificativa do Cancelamento |
| IdeRet | String(300) | Sim | Identificador de Retorno |
| MsgRet | String(2000) | Sim | Mensagem de Retorno |
| TipOpe | String(001) | Sim | Tipo de Operação |
| DatEnv | Date | Sim | Data do último envio |
| CmpAu1 | Date | Sim | Campo Auxiliar 1 |
| CmpAu2 | Date | Sim | Campo Auxiliar 2 |
| CmpAu3 | Number(008,0) | Sim | Campo Auxiliar 3 |
| CmpAu4 | Number(008,0) | Sim | Campo Auxiliar 4 |
| CmpAu5 | Number(008,0) | Sim | Campo Auxiliar 5 |
| CmpAu6 | Number(008,0) | Sim | Campo Auxiliar 6 |
| CmpAu7 | String(002) | Sim | Campo Auxiliar 7 |
| CmpAu8 | String(002) | Sim | Campo Auxiliar 8 |
| CmpAu9 | String(2000) | Sim | Campo Auxiliar 9 |

---

## Chave Primária

- NumEmp
- NumEdi
- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
