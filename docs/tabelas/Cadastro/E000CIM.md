# E000CIM

## Descrição

Tabelas - Integrações - Controle de Importações

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodInt | Number(002,0) | Não | Código da Integração |
| IdeInt | Number(009,0) | Não | Código Identificador do tipo de informação |
| IdtReq | String(020) | Não | Identificação da requisição |
| ChvReq | String(020) | Sim | Chave da requisição, gravada na R960PAR (idReq) |
| DatReq | Date | Sim | Data em que foi efetuada a requisição |
| HorReq | Number(005,0) | Sim | Hora em que foi efetuada a requisição |
| XmlRet | Image | Sim | XML de Retorno da requisição |

---

## Chave Primária

- CodEmp
- CodFil
- CodInt
- IdeInt
- IdtReq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
