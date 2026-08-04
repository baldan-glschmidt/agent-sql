# E080TXM

## Descrição

Cadastros - Serviços - Ligação Tipo de Serviço X Município

---

## Resumo

- Campos: 18
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| SerImp | String(010) | Não | Tipo de Serviço no contexto fiscal baseado na LC 116/2003 |
| CodRai | Number(007,0) | Não | Código da cidade para a RAIS |
| DatIni | Date | Não | Data de início da vigência |
| PerIss | Number(006,4) | Sim | Percentual do ISS previsto para venda do serviço no CEP |
| CodFim | String(010) | Sim | Código fiscal municipal do serviço |
| TriNfs | String(020) | Sim | Código de tributação do serviço para nota fiscal de serviço eletrônica |
| CstIss | String(010) | Sim | Situação tributária do ISS do serviço |
| RedIss | Number(008,5) | Sim | Percentual de redução da base de cálculo do ISS de entrada |
| RedIsv | Number(008,5) | Sim | Percentual de redução da base de cálculo do ISS de saída |
| PerIsc | Number(006,4) | Sim | Percentual do ISS para o Simples Nacional |
| PerLdm | Number(005,2) | Sim | Percentual do limite de dedução de material utilizado na prestação do serviço |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- SerImp
- CodRai
- DatIni

---

## Índices

### E080TXMIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- TriNfs

---

## Relacionamentos

Nenhum relacionamento cadastrado.
