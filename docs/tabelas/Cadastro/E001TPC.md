# E001TPC

## Descrição

Tabelas - Transação - Parâmetros Complementares (GO UP)

---

## Resumo

- Campos: 20
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação |
| SeqTns | Number(004,0) | Não | Sequência da ligação |
| TipNfe | Number(002,0) | Sim | Tipo de nota fiscal de entrada |
| TipNfs | Number(002,0) | Sim | Tipo da nota fiscal de saída |
| BxaInc | String(001) | Não | Indicativo se permite baixa ou inclusão manual CR e CP |
| VlrBxa | String(001) | Não | Valor do movimento deve ser igual ao valor líquido nas baixas CR e CP |
| RatPrd | String(001) | Não | Indicativo que a transação utiliza rateio pré definido |
| FilMov | String(001) | Não | Indicativo se é permitido utilizar filial diferente entre movimentos de CR ou CP |
| FilCta | String(001) | Não | Indicativo se permite filial do movimento diferente da filial da conta interna |
| DepTns | String(001) | Não | Indicativo se é obrigatória a ligação do depósito X transação |
| VinNfi | String(001) | Não | Indicativo se é obrigatório o vínculo da Nfe X Nfs (ou vice versa) |
| ExiHob | String(001) | Não | Indicativo se é obrigatório o uso de histórico/observação |
| EscIpi | String(001) | Não | Indicativo da forma de escrituração do IPI na transação |
| EscIcm | String(001) | Não | Indicativo da forma de escrituração do ICMS na transação |
| VlrCtb | String(250) | Sim | Endereço de busca do valor contábil para contabilização por custo/despesa |
| SitTpc | String(001) | Não | Situação do parâmetro complementar da transação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodTns
- SeqTns

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
