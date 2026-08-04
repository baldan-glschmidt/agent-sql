# E080SXC

## Descrição

Cadastros - Serviços - Ligação Serviço X CEP

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodSer | String(014) | Não | Código do serviço |
| CepIni | Number(008,0) | Não | Faixa inicial do CEP da cidade |
| DatIni | Date | Não | Data de início da vigência |
| PerIss | Number(006,4) | Sim | Percentual do ISS previsto para venda do serviço no CEP |
| CodFim | String(010) | Sim | Código fiscal municipal do serviço |
| TriNfs | String(020) | Sim | Código de tributação do serviço para nota fiscal de serviço eletrônica |
| CstIss | String(010) | Sim | Situação tributária do ISS do serviço |
| RedIss | Number(008,5) | Sim | Percentual de redução da base de cálculo do ISS de entrada |
| RedIsv | Number(008,5) | Sim | Percentual de redução da base de cálculo do ISS de saída |
| PerIsc | Number(006,4) | Sim | Percentual do ISS para o Simples Nacional |

---

## Chave Primária

- CodEmp
- CodSer
- CepIni
- DatIni

---

## Índices

### E080SXCIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- TriNfs

---

## Relacionamentos

Nenhum relacionamento cadastrado.
