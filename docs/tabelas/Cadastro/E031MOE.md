# E031MOE

## Descrição

Tabelas - Moedas

---

## Resumo

- Campos: 19
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMoe | String(003) | Não | Código da moeda ou índice |
| DesMoe | String(030) | Não | Descrição da moeda ou índice |
| SigMoe | String(005) | Não | Sigla da moeda ou índice |
| TipMoe | String(001) | Não | Tipo de moeda |
| TipCot | String(001) | Não | Tipo de cotação |
| DiaBas | Number(002,0) | Sim | Quando tipo de cotação = M, informar dia base da cotação mensal |
| QtdInt | Number(002,0) | Sim | Número de posições inteiras para a moeda |
| QtdDec | Number(002,0) | Sim | Número de posições decimais para a moeda |
| IdeSmo | Number(009,0) | Sim | Identificador da série da moeda |
| TipInm | Number(002,0) | Sim | Tipo da integração da moeda |
| CodNeg | String(012) | Sim | Código da negociação do papel |
| PraZot | String(003) | Sim | Prazo em dias do mercado a termo |
| CodSel | Number(009,0) | Sim | Código selic do título público |
| DatEmi | Date | Sim | Data da emissão do título público |
| DatVct | Date | Sim | Data do vencimento do título público |
| CodBac | Number(003,0) | Sim | Código da moeda para o BACEN |
| IntAgr | String(001) | Sim | Indica se o registro integra no App do Produtor |
| TipCon | String(060) | Sim | Tipo de Conversão da Moeda |
| IntAcp | String(001) | Sim | Habilitar integração com Antecipação Contas a Pagar |

---

## Chave Primária

- CodMoe

---

## Índices

### E031MOEIndice2

**Tipo:** Não unico

Campos:
- CodSel
- DatEmi
- DatVct

---

## Relacionamentos

Nenhum relacionamento cadastrado.
