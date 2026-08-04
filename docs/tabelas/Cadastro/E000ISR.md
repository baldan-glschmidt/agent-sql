# E000ISR

## Descrição

Recebimento de Documentos Eletrônicos - Notas de Entrada - Itens de Serviço - Reforma tributária

---

## Resumo

- Campos: 25
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CgcFil | Number(015,0) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| DocIdeFil | String(014) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| CgcFor | Number(014,0) | Sim | Número do CNPJ ou CPF do fornecedor |
| DocIdeFor | String(014) | Sim | Número do CNPJ ou CPF do fornecedor |
| ChvNel | String(050) | Não | Chave de acesso da nota fiscal eletrônica |
| SeqIsc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| IdeScr | Number(009,0) | Não | Identificador do cClassTrib |
| CodImp | String(003) | Não | Código do imposto |
| BasCal | Number(015,4) | Sim | Base Cálculo |
| AliImp | Number(007,4) | Sim | Percentual da Alíquota |
| PerDif | Number(007,4) | Sim | Percentual de Diferimento |
| VlrDif | Number(013,2) | Sim | Valor Diferimento |
| PerRed | Number(007,4) | Sim | Percentual de Redução |
| AliEfe | Number(007,4) | Sim | Alíquota Efetiva |
| IdeStr | Number(009,0) | Sim | cClassTrib de Trib. Regular caso não cumprida condição resolutiva/suspensiva |
| PerDes | Number(007,4) | Sim | Percentual de Tributação Regular |
| VlrDes | Number(013,2) | Sim | Valor de Tributação Regular |
| VlrImp | Number(013,2) | Sim | Valor Imposto |
| CodPci | String(003) | Sim | Código Interno |
| PerPci | Number(008,4) | Sim | Percentual do crédito presumido |
| VlrPci | Number(013,2) | Sim | Valor do crédito presumido |
| ConSus | String(001) | Sim | Crédito presumido em condição suspensiva |
| DedCre | String(001) | Sim | Deduz o valor do crédito presumido do valor total |
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| IdeIsc | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeUni

---

## Índices

### E000ISRIndice1

**Tipo:** Não unico

Campos:
- DocIdeFil
- DocIdeFor
- ChvNel
- SeqIsc
- CodImp

### E000ISRIndice2

**Tipo:** Não unico

Campos:
- CgcFil
- CgcFor
- ChvNel
- SeqIsc
- CodImp

### E000ISRIndice3

**Tipo:** Não unico

Campos:
- IdeIsc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
