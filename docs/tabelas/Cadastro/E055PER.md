# E055PER

## Descrição

Cadastros - Tributos - Parâmetros das Exceções dos Impostos de Retenção

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatRef | Date | Não | Competência Início |
| Codtns | String(005) | Não | Código da transação |
| CodPro | String(014) | Sim | Código do produto |
| CodSer | String(014) | Sim | Código do serviço |
| CodCli | Number(009,0) | Sim | Código do Cliente |
| CodFor | Number(009,0) | Sim | Código do Fornecedor |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E055PERIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodImp
- DatRef
- Codtns
- CodPro
- CodSer
- CodCli
- CodFor

---

## Relacionamentos

### IR_E055PER_003

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

