# E080SXT

## Descrição

Cadastros - Serviços - Ligação Serviço X Transação

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodSer | String(014) | Não | Código do serviço |
| CodTns | String(005) | Não | Código da transação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodSer
- CodTns

---

## Índices

### E080SXTIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodTns

---

## Relacionamentos

### IR_E080SXT_001

**Tabela:** E080SER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodSer | CodSer |

### IR_E080SXT_002

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

