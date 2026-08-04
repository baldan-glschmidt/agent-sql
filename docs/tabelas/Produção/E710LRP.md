# E710LRP

## Descrição

Ficha - Roteiro - Liga Roteiro X Produto

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodPro | String(014) | Não | Código do Produto Composto associado ao Roteiro |
| CodDer | String(007) | Não | Código da derivação do Produto (tamanho, cor, etc.) |
| CodRot | String(014) | Não | Código do Roteiro de Produção |
| CodEtg | Number(004,0) | Não | Código do estágio de produção para execução da operação |
| SfxEtr | Number(003,0) | Não | Opção do estágio (1=Padrão, 2-999=Alternativas) |
| SeqRot | Number(004,0) | Não | Sequência lógica da operação no roteiro de produção |
| SfxSeq | Number(002,0) | Não | Opção da sequência (1=Padrão, 2-99=Alternativas) |
| CodUsu | Number(010,0) | Sim | Código do Usuário que alterou |
| DatAlt | Date | Sim | Data da Geração ou Alteração da ligação Modelo X Produto |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodRot
- CodEtg
- SfxEtr
- SeqRot
- SfxSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E710LRP_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E710LRP_003

**Tabela:** E710ROT

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodRot | CodRot |

### IR_E710LRP_005

**Tabela:** E710ETR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodRot | CodRot |
| CodEtg | CodEtg |
| SfxEtr | SfxEtr |

