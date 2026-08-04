# E710SRF

## Descrição

Ficha - Ligação Seq. Roteiro com Ferramentas

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodRot | String(014) | Não | Código do roteiro de produção associado ao produto |
| CodEtg | Number(004,0) | Não | Código do estágio de produção para execução da operação |
| SfxEtr | Number(003,0) | Não | Opção do estágio (1=Padrão, 2-999=Alternativas) |
| SeqRot | Number(004,0) | Não | Sequência lógica da operação no roteiro de produção |
| SfxSeq | Number(002,0) | Não | Opção da sequência (1=Padrão, 2-99=Alternativas) |
| CodFrt | String(014) | Não | Código da Ferramenta |
| DerFrt | String(007) | Não | Código da derivação da Ferramenta |
| QtdFrt | Number(004,0) | Não | Quantidade de ferramentas necessárias |
| ObsSrf | String(240) | Sim | Observações |

---

## Chave Primária

- CodEmp
- CodRot
- CodEtg
- SfxEtr
- SeqRot
- SfxSeq
- CodFrt
- DerFrt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E710SRF_003

**Tabela:** E710ETR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodRot | CodRot |
| CodEtg | CodEtg |
| SfxEtr | SfxEtr |

