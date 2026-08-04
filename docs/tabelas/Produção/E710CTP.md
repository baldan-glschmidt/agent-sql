# E710CTP

## Descrição

Ficha - Roteiro - Cálculo de Tempo da Seqüência Operacional

---

## Resumo

- Campos: 17
- Chave Primária: 7 campo(s)
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
| CodOpr | String(006) | Não | Código da operação |
| SeqCtp | Number(004,0) | Sim | Seqüência de inclusão da operação p/ efeito de ordenação |
| VlrVa1 | Number(014,5) | Sim | Valor da variável p/ cálculo de tempo da operação informada |
| VlrVa2 | Number(014,5) | Sim | Valor da variável p/ cálculo de tempo da operação informada |
| VlrVa3 | Number(014,5) | Sim | Valor da variável p/ cálculo de tempo da operação informada |
| VlrVa4 | Number(014,5) | Sim | Valor da variável p/ cálculo de tempo da operação informada |
| VlrVa5 | Number(014,5) | Sim | Valor da variável p/ cálculo de tempo da operação informada |
| VlrVa6 | Number(014,5) | Sim | Valor da variável p/ cálculo de tempo da operação informada |
| VlrVa7 | Number(014,5) | Sim | Valor da variável p/ cálculo de tempo da operação informada |
| DatAlt | Date | Não | Data de geração/alteração do cálculo |
| CodUsu | Number(010,0) | Sim | Usuário que gerou/alterou |

---

## Chave Primária

- CodEmp
- CodRot
- CodEtg
- SfxEtr
- SeqRot
- SfxSeq
- CodOpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E710CTP_005

**Tabela:** E710SQR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodRot | CodRot |
| CodEtg | CodEtg |
| SfxEtr | SfxEtr |
| SeqRot | SeqRot |
| SfxSeq | SfxSeq |

### IR_E710CTP_006

**Tabela:** E720OPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOpr | CodOpr |

