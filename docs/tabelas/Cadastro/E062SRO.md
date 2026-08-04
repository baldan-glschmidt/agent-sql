# E062SRO

## Descrição

Tabelas - Sub Rotas

---

## Resumo

- Campos: 18
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRoe | String(003) | Não | Código da Rota ou Localidade |
| CodSro | String(003) | Não | Código da Sub Rota |
| DesRoe | String(030) | Não | Descrição da Sub Rota |
| MaxEnt | Number(004,0) | Sim | Número máximo de entregas no dia |
| KmtTot | Number(008,2) | Sim | Quilometragem total da Rota |
| CepIni | Number(008,0) | Sim | CEP Inicial |
| CepFim | Number(008,0) | Sim | CEP Final |
| HorRoe | Number(004,0) | Sim | Tempo da Rota em Horas. |
| SitSro | String(001) | Sim | Situação da sub rota |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pelo geração do registro |
| DatGer | Date | Sim | Data do cadastro do registro |
| HorGer | Number(005,0) | Sim | Hora do cadastro do registro |
| UsuAlt | Number(010,0) | Sim | Código do usuário responsável pelo alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| CodFor | Number(009,0) | Sim | Código do fornecedor |
| FilRoe | Number(005,0) | Sim | Código da filial |
| VlrAdr | Number(015,2) | Sim | Valor adicional da subrota a ser pago ao motorista |

---

## Chave Primária

- CodRoe
- CodSro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
