# E080CSI

## Descrição

Tabelas - Serviços - Cadastro de serviços intermediados

---

## Resumo

- Campos: 18
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| SeqCsi | Number(004,0) | Não | Sequencia do serviço |
| DatIni | Date | Não | Data da validade inicial do seguro |
| DatFim | Date | Não | Data da validade final do seguro |
| SitReg | String(001) | Não | Situação do registro |
| TipSin | Number(001,0) | Não | Tipo de serviço intermediado |
| CodSer | String(014) | Sim | Código de serviço para gravação em nota de venda |
| IdeFor | String(020) | Sim | Identificação no fornecedor |
| DesCsi | String(050) | Sim | Descrição do serviço |
| PerIof | Number(005,2) | Sim | Percentual de IOF aplicado sobre o prêmio |
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

### E080CSIIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFor
- SeqCsi

### E080CSIIndice2

**Tipo:** Não unico

Campos:
- CodFor

---

## Relacionamentos

### IR_E080CSI_002

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

