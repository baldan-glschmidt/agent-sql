# E031IMH

## Descrição

Tabelas - Moedas - Índices por Hora

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMoe | String(003) | Não | Código da moeda ou índice |
| DatMoe | Date | Não | Data da cotação da moeda ou índice |
| HorCot | Number(005,0) | Não | Hora da cotação do registro |
| VlrCot | Number(019,10) | Sim | Valor da cotação |
| VlrPre | Number(019,10) | Sim | Valor de previsão |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |

---

## Chave Primária

- CodMoe
- DatMoe
- HorCot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E031IMH_000

**Tabela:** E031MOE

| Origem | Destino |
|--------|---------|
| CodMoe | CodMoe |

