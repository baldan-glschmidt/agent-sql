# E002RXT

## Descrição

Cadastros - Finanças - Contas a Pagar/Receber - Relacionamento entre Tipo de Título

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 3
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpt | String(003) | Não | Código do tipo do título |
| TptRlc | String(003) | Não | Código do tipo do título relacionado |
| TipRtt | Number(001,0) | Não | Indicativo da aplicação do relacionamento entre tipo de título |
| SitRxt | String(001) | Não | Situação do relacionamento |
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
- TptRlc

---

## Índices

### E002RXTIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- SitRxt

### E002RXTIndice3

**Tipo:** Não unico

Campos:
- CodTpt

### E002RXTIndice4

**Tipo:** Não unico

Campos:
- TptRlc

---

## Relacionamentos

### IR_E002RXT_001

**Tabela:** E002TPT

| Origem | Destino |
|--------|---------|
| CodTpt | CodTpt |

### IR_E002RXT_002

**Tabela:** E002TPT

| Origem | Destino |
|--------|---------|
| TptRlc | CodTpt |

