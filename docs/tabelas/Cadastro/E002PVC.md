# E002PVC

## Descrição

Cadastros - Finanças - Parâmetros Variação Cambial

---

## Resumo

- Campos: 28
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador dos parâmetros da variação cambial |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SitReg | String(001) | Não | Situação do registro |
| AplPar | String(001) | Sim | Indica o módulo de destino dos parâmetros |
| VlrMin | Number(015,2) | Sim | Valor mínimo do título para o cálculo da variação cambial |
| QtdTpc | Number(009,0) | Não | Quantidade de títulos por pacote de processamento do cálculo |
| TipCal | String(001) | Não | Tipo de cálculo do valor de atualização da variação cambial |
| TnsPos | String(005) | Não | Transação padrão para atualização de variação cambial positiva do título |
| TnsNeg | String(005) | Não | Transação padrão para atualização de variação cambial negativa do título |
| TnsEps | String(005) | Não | Transação padrão para estorno da atualização de variação cambial positiva do título |
| TnsEng | String(005) | Não | Transação padrão para estorno da atualização de variação cambial negativa do título |
| TnsPsc | String(005) | Não | Transação padrão para atualização de variação cambial positiva na correção monetária |
| TnsNgc | String(005) | Não | Transação padrão para atualização de variação cambial negativa na correção monetária |
| TnsEpc | String(005) | Não | Transação padrão para estorno da atualização de variação cambial positiva na correção monetária |
| TnsEnc | String(005) | Não | Transação padrão para estorno da atualização de variação cambial negativa na correção monetária |
| TnsPsi | String(005) | Não | Transação padrão para atualização de variação cambial positiva da conta interna |
| TnsNgi | String(005) | Não | Transação padrão para atualização de variação cambial negativa da conta interna |
| TnsEpi | String(005) | Não | Transação padrão para estorno da atualização de variação cambial positiva da conta interna |
| TnsEni | String(005) | Não | Transação padrão para estorno da atualização de variação cambial negativa da conta interna |
| TnsBpp | String(005) | Não | Transação padrão para atualização de variação cambial positiva na baixa parcial do título |
| TnsBpn | String(005) | Não | Transação padrão para atualização de variação cambial negativa na baixa parcial do título |
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

### E002PVCIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- AplPar

---

## Relacionamentos

Nenhum relacionamento cadastrado.
