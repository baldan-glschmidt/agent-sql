# E085CNV

## Descrição

Cadastros - Clientes - Convênio

---

## Resumo

- Campos: 13
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodCnv | Number(004,0) | Não | Código do convênio |
| NumCcn | String(020) | Sim | Número do cartão do convênio |
| LimCre | Number(015,2) | Sim | Limite de crédito do convênio do cliente |
| CreUti | Number(015,2) | Sim | Exibe o quanto do limite de crédito foi utilizado |
| SitCnv | String(001) | Não | Situação do convênio (Ativo ou Inativo) |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAtu | Date | Sim | Data da última alteração do registro |
| HorAtu | Number(005,0) | Sim | Hora da última alteração do registro |
| SenCnv | String(020) | Sim | Senha do conveniado no convênio |

---

## Chave Primária

- CodCli
- CodCnv

---

## Índices

### E085CNVIndice1

**Tipo:** Não unico

Campos:
- CodCnv

---

## Relacionamentos

### IR_E085CNV_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

### IR_E085CNV_001

**Tabela:** E069CNV

| Origem | Destino |
|--------|---------|
| CodCnv | CodCnv |

