# E002TXT

## Descrição

Cadastros - Finanças - Contas a Pagar/Receber - Relacionamento Tipo de Título X  Transação

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpt | String(003) | Não | Código do tipo do título a pagar |
| CodTns | String(005) | Não | Código da transação |
| SitTxt | String(001) | Não | Situação do relacionamento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodTpt
- CodTns

---

## Índices

### E002TXTIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- SitTxt

### E002TXTIndice3

**Tipo:** Não unico

Campos:
- CodTpt

---

## Relacionamentos

### IR_E002TXT_001

**Tabela:** E002TPT

| Origem | Destino |
|--------|---------|
| CodTpt | CodTpt |

