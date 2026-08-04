# E120EMB

## Descrição

Vendas - Pedidos - Embalagens

---

## Resumo

- Campos: 21
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqEmb | Number(006,0) | Não | Sequência de embalagem |
| CodEmb | Number(004,0) | Sim | Código da embalagem |
| QtdEmb | Number(006,0) | Sim | Quantidade de embalagens |
| NumEmb | String(030) | Sim | Números das embalagens |
| NumNiv | Number(002,0) | Sim | Nível da Embalagem |
| VolOcu | Number(009,3) | Sim | Volume já ocupado da embalagem |
| PesBru | Number(014,5) | Sim | Peso bruto das embalagens e produtos |
| PesLiq | Number(014,5) | Sim | Peso líquido dos produtos |
| ObsEmb | String(250) | Sim | Texto da observação das embalagens |
| SitEmb | Number(001,0) | Sim | Situação da Embalagem |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro ou entrada caminhão |
| DatGer | Date | Sim | Data da geração do registro ou entrada do caminhão |
| HorGer | Number(005,0) | Sim | Hora da geração do registro ou entrada do caminhão |
| CodFxa | String(015) | Sim | Código da faixa da grade da embalagem |
| CodPgr | String(005) | Sim | Código da Proporcionalidade da Grade de Derivações |
| IdxGrd | Number(006,0) | Sim | Indexador da Grade a que se refere esta embalagem |
| CodOri | String(003) | Sim | Código da Origem do Produto |
| NumOrp | Number(009,0) | Sim | Número da Ordem de Produção |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqEmb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
