# E075PXT

## Descrição

Cadastros - Produtos - Ligação Produto X Transação

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodTns | String(005) | Não | Código da transação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| CodEnq | Number(003,0) | Sim | Código de enquadramento legal do IPI |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |

---

## Chave Primária

- CodEmp
- CodPro
- CodTns

---

## Índices

### E075PXTIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodTns

---

## Relacionamentos

### IR_E075PXT_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E075PXT_002

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

