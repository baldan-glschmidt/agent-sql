# E710APL

## Descrição

Ficha - Roteiro - Aplicações de Componentes na Seqüência Operacional

---

## Resumo

- Campos: 13
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodRot | String(014) | Não | Código do roteiro de produção associado ao produto |
| CodEtg | Number(004,0) | Não | Código do estágio de produção para execução da operação |
| SfxEtr | Number(003,0) | Não | Opção do estágio (1=Padrão, 2-999=Alternativas) |
| SeqRot | Number(004,0) | Não | Seqüência lógica da operação no roteiro de produção |
| SfxSeq | Number(002,0) | Não | Opção da seqüência (1=Padrão, 2-99=Alternativas) |
| CodMod | String(014) | Não | Código do modelo associado ao produto |
| SeqMod | Number(004,0) | Não | Seqüência lógica que o componente é utilizado na fabricação do produto composto |
| ObsApl | String(240) | Sim | Observações |
| DatAlt | Date | Não | Data de geração/alteração da seqüência |
| HorAlt | Number(005,0) | Sim | Hora da geração/alteração do registro |
| CodUsu | Number(010,0) | Sim | Usuário que alterou |
| USU_qtdapl | Number(004,0) | Sim | Quantidades de Pecas Aplicadas para o Produto no Roteiro |

---

## Chave Primária

- CodEmp
- CodRot
- CodEtg
- SfxEtr
- SeqRot
- SfxSeq
- CodMod
- SeqMod

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E710APL_003

**Tabela:** E710ETR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodRot | CodRot |
| CodEtg | CodEtg |
| SfxEtr | SfxEtr |

### IR_E710APL_006

**Tabela:** E700MOD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMod | CodMod |

