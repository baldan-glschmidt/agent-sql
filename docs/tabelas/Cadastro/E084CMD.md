# E084CMD

## Descrição

Cadastros - Máscara Derivação - Componentes

---

## Resumo

- Campos: 14
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodMdp | String(008) | Não | Código  da Máscara Derivação |
| CodDer | String(007) | Não | Código da Derivação p/ utilizar no Produto |
| SeqCmd | Number(007,0) | Não | Ordenação Sequencial  da Derivação |
| DesDer | String(050) | Não | Descrição do Componente da Máscara |
| AbrDer | String(040) | Não | Abreviatura do Componente da Máscara |
| CodAgr | Number(004,0) | Sim | Código do  agrupamento  de Derivações  p/  Produto. |
| SitCmd | String(001) | Não | Situação do componente da máscara de derivação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodMdp
- CodDer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E084CMD_001

**Tabela:** E084MDP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMdp | CodMdp |

