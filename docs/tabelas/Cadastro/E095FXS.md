# E095FXS

## Descrição

Cadastros - Fornecedores - Ligação Fornecedor X Série

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFor | Number(009,0) | Não | Código do fornecedor |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| CodSel | String(020) | Sim | Código da Série Legal |
| CodSsl | String(002) | Sim | Código da Subsérie Legal |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodFor
- CodEmp
- CodFil
- CodSnf

---

## Índices

### E095FXSIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSnf

---

## Relacionamentos

### IR_E095FXS_002

**Tabela:** E095HFO

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E095FXS_003

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

